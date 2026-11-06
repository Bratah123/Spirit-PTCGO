from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _DragonDance(Passive):
    """As long as this Haxorus is your Active Pokemon, its attacks do 100 more (max +100)."""
    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if me is None or calc.attacker is not me or not calc.is_attack or calc.target is None:
            return
        opp = calc.target.owning_player_id
        if (opp == me.owning_player_id or calc.board.active_pokemon(opp) is not calc.target
                or calc.board.active_pokemon(me.owning_player_id) is not me):
            return
        calc.amount += 100


async def _dragon_dance(ctx):
    """While this Haxorus stays your Active, each of its attacks does 100 more
    (the boost does not stack on repeat use)."""
    for tp in ctx.board.temporary_passives:
        if tp.carrier_entity_id == ctx.attacker.entity_id and isinstance(tp.passive, _DragonDance):
            return
    ctx.add_temporary_passive(ctx.attacker, _DragonDance())


card = PokemonCardDef(
    guid="9bcd06ba-9d3a-5c2a-9cfa-2afad9e850d9",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haxorus.Name",
    display_name="Haxorus",
    searchable_by=["Haxorus", "Stage 2", "Haxorus"],
    subtypes=["Stage 2"],
    collector_number=111,
    set_code="XY8",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    family_id=610,
    abilities=[
        Attack(
            title="Dragon Dance",
            game_text="As long as this Haxorus is your Active Pok\u00e9mon, each of its attacks does 100 more damage (before applying Weakness and Resistance). You can't add more than 100 damage in this way.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_dragon_dance,
        ),
        Attack(
            title="Sharp Fang",
            cost={PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 3 cards of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=130,
            effect=mill_attack(3, opponent=False),
        ),
    ],
)