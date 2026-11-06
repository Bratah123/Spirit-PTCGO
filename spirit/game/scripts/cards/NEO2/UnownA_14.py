from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_anger_passive


card = PokemonCardDef(
    guid="82a84024-2206-5687-9220-164800a48ef8",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownA.Name",
    display_name="Unown [A]",
    searchable_by=["Unown [A]", "Basic", "UnownA"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Anger]",
            game_text="Whenever 1 of your Pok\u00e9mon with Unown in its name uses its Hidden Power attack, that attack does 10 more damage for each damage counter on Unown [A]. If you have more than 1 Unown [A] in play, use only 1 [Anger] for each attack.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_anger_passive,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
