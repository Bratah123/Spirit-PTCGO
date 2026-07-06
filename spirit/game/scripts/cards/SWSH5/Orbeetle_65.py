from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cae6af0b-3116-57b0-83bb-99cd9619cae0",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orbeetle.Name",
    display_name="Orbeetle",
    searchable_by=["Orbeetle", "Stage 2", "Orbeetle"],
    subtypes=["Stage 2"],
    collector_number=65,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dottler.Name",
    family_id=824,
    abilities=[
        Attack(
            title="Evomancy",
            game_text="For each Energy attached to this Pok\u00e9mon, search your deck for a Stage 2 Pok\u00e9mon, except Orbeetle, and put it onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)