from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="9a697802-b4c0-5b83-a8eb-ef72192c2406",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Ability(
            title="Sturdy",
            game_text="If this Pok\u00e9mon has full HP and would be Knocked Out by damage from an attack, this Pok\u00e9mon is not Knocked Out and its remaining HP becomes 10 instead.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Stone Edge",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)