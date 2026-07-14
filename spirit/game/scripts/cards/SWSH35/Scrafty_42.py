from spirit.game.card_effects.attacks_common import bonus_if
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

_played_piers_this_turn = lambda ctx: ctx.played_trainer_this_turn("Piers") > 0


async def corner(ctx):
    """30 damage; the Defending Pokemon can't retreat during your opponent's next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        ctx.lock_retreat(defender)


card = PokemonCardDef(
    guid="6675e84d-50f9-5bad-881d-1bf39c83c4ba",
    key="SWSH35",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty", "Stage 1", "Scrafty"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="SWSH35",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    family_id=559,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=corner,
        ),
        Attack(
            title="Bad Brawl",
            game_text="If you played Piers from your hand during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            damage_operator="+",
            effect=bonus_if(_played_piers_this_turn, 90),
        ),
    ],
)