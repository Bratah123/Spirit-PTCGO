from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="76171ee9-444f-55b9-be06-dba5a2558e64",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name",
    display_name="Zubat",
    searchable_by=["Zubat", "Basic", "Zubat"],
    subtypes=["Basic"],
    collector_number=53,
    set_code="BW8",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=41,
    abilities=[
        Ability(
            title="Free Flight",
            game_text="If this Pok\u00e9mon has no Energy attached to it, this Pok\u00e9mon has no Retreat Cost.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Wing Attack",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)