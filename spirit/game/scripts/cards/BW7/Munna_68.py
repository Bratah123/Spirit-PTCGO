from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="84d781a9-306b-5923-b098-889669e17382",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Munna.Name",
    display_name="Munna",
    searchable_by=["Munna", "Basic", "Munna"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=517,
    abilities=[
        Ability(
            title="Long-Distance Hypnosis",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Asleep. If tails, your Active Pok\u00e9mon is now Asleep.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Psyshot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)