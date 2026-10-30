from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import baton_pass


card = PokemonCardDef(
    guid="02f01cb0-530d-5e84-8550-4e848b40082c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1", "Ledian"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Attack(
            title="Baton Pass",
            game_text="If you have any Grass Pok\u00e9mon on your Bench, remove all Grass Energy cards from Ledian and attach them to 1 of those Pok\u00e9mon, then switch Ledian with that Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=baton_pass,
        ),
    ],
)
