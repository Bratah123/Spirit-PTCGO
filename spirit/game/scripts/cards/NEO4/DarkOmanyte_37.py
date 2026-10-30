from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import water_cannon


card = PokemonCardDef(
    guid="15c37cb0-c937-5b5f-847e-1039f59af649",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkOmanyte.Name",
    display_name="Dark Omanyte",
    searchable_by=["Dark Omanyte", "Stage 1", "DarkOmanyte"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MysteriousFossil.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Water Cannon",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage for each Water Energy card attached to Dark Omanyte. Don't apply Weakness and Resistance. You can't do more than 30 damage in this way.",
            cost={PokemonTypes.WATER: 1},
            effect=water_cannon,
        ),
    ],
)
