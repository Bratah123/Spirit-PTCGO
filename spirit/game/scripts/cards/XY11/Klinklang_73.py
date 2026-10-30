from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, effective_retreat_cost, carrier_pokemon
from spirit.game.card_effects.passives_common import boost_own_next_turn


class _HeavyBumper(Passive):
    """Opponent's attack damage to this Pokemon is reduced by 10 per Colorless
    in the opponent's Active's Retreat Cost (after W/R)."""
    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and calc.target is me and calc.amount > 0):
            return
        active = calc.board.active_pokemon(calc.attacker.owning_player_id) if calc.attacker else None
        if active is not None:
            calc.amount = max(0, calc.amount - 10 * effective_retreat_cost(calc.board, active))


card = PokemonCardDef(
    guid="7f760b93-7cb6-52ea-8283-0dadcdcfbd8d",
    key="XY11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2", "Klinklang"],
    subtypes=["Stage 2"],
    collector_number=73,
    set_code="XY11",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Heavy Bumper",
            game_text="Any damage done to this Pok\u00e9mon by an opponent's attack is reduced by 10 for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost (after applying Weakness and Resistance).",
            passive=_HeavyBumper(),
        ),
        Attack(
            title="Gear Spinner",
            game_text="During your next turn, this Pok\u00e9mon's Gear Spinner attack does 70 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=boost_own_next_turn(70, 'Gear Spinner'),
        ),
    ],
)