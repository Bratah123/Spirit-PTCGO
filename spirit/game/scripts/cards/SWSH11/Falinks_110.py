from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import defender_is_v


async def fighting_headbutt(ctx):
    """10, +50 vs a Pokémon V; not affected by Weakness."""
    bonus = 50 if defender_is_v(ctx) else 0
    await ctx.deal_damage(10 + bonus, ignore_weakness=True)

card = PokemonCardDef(
    guid="d287bd67-a29a-5307-baee-39a1f3f27da7",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Falinks.Name",
    display_name="Falinks",
    searchable_by=["Falinks", "Basic", "Falinks"],
    subtypes=["Basic"],
    collector_number=110,
    set_code="SWSH11",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=870,
    abilities=[
        Attack(
            title="Fighting Headbutt",
            game_text="This attack's damage isn't affected by Weakness. If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon V, this attack does 50 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=fighting_headbutt,
        ),
        Attack(
            title="Jet Headbutt",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)