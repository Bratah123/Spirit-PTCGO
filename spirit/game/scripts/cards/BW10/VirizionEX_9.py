from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="d0122962-d935-5e0d-a9de-3ae8b0465185",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VirizionEX.Name",
    display_name="Virizion-EX",
    searchable_by=["Virizion-EX", "Basic", "EX", "VirizionEX"],
    subtypes=["Basic", "EX"],
    collector_number=9,
    set_code="BW10",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=640,
    abilities=[
        Ability(
            title="Verdant Wind",
            game_text="Each of your Pok\u00e9mon that has any Grass Energy attached to it can't be affected by any Special Conditions. (Remove any Special Conditions affecting those Pok\u00e9mon.)",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Emerald Slash",
            game_text="You may search your deck for 2 Grass Energy cards and attach them to 1 of your Benched Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)