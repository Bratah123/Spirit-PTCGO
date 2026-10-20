from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _telekinesis(ctx):
    """20 damage to 1 of the opponent's Pokemon, not affected by Weakness or Resistance."""
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    t = pool[0] if len(pool) == 1 else await ctx.choose_pokemon(pool, "Choose a Pokémon to take 20 damage")
    if t is not None:
        await ctx.deal_damage(20, target=t, ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="2cdfa24a-4fa1-5a4f-9990-f05011e0b10c",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    display_name="Team Magma's Baltoy",
    searchable_by=["Team Magma's Baltoy", "Basic", "TeamMagmasBaltoy"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="TATM",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=343,
    abilities=[
        Attack(
            title="Telekinesis",
            game_text="This attack does 20 damage to 1 of your opponent's Pok\u00e9mon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_telekinesis,
        ),
    ],
)