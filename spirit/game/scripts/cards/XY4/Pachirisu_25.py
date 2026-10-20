from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.session.passives import Passive, carrier_pokemon


class _TrickSticker(Passive):
    """This Pokemon's Weakness is now Lightning (same amount)."""
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier) and calc.weak_types:
            calc.weak_types = [PokemonTypes.LIGHTNING.value]


async def _trick_sticker(ctx):
    """10; the Defending Pokemon's Weakness is Lightning until the end of your next turn."""
    await ctx.deal_damage()
    d = ctx.defender
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_own_next_turn(d, _TrickSticker())


card = PokemonCardDef(
    guid="de8bb130-33bc-5795-8485-0f52d2f98707",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=417,
    abilities=[
        Attack(
            title="Trick Sticker",
            game_text="The Defending Pok\u00e9mon's Weakness is now Lightning until the end of your next turn. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=_trick_sticker,
        ),
        Attack(
            title="Pachi",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)