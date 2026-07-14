from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy
from spirit.game.card_effects.passives_common import condition_immunity_passive

card = PokemonCardDef(
    guid="ce15658e-4699-5663-978e-87cd51033118",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianRapidash.Name",
    display_name="Galarian Rapidash",
    searchable_by=["Galarian Rapidash", "Stage 1", "GalarianRapidash"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SWSH1",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianPonyta.Name",
    family_id=77,
    abilities=[
        Ability(
            title="Pastel Veil",
            game_text="Your Pok\u00e9mon recover from all Special Conditions and can't be affected by any Special Conditions.",
            passive=condition_immunity_passive(protects="team"),
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 30 more damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 30, base=30),
        ),
    ],
)