from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="ee422255-ef19-5248-98b7-4d7d3eed04c9",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysEX.Name",
    display_name="Deoxys-EX",
    searchable_by=["Deoxys-EX", "Basic", "EX", "Team Plasma", "DeoxysEX"],
    subtypes=["Basic", "EX", "Team Plasma"],
    collector_number=53,
    set_code="BW9",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=386,
    abilities=[
        Ability(
            title="Power Connect",
            game_text="Your Team Plasma Pok\u00e9mon's attacks (excluding Deoxys-EX) do 10 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Helix Force",
            game_text="If this Pok\u00e9mon has any Plasma Energy attached to it, this attack does 30 more damage for each Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)