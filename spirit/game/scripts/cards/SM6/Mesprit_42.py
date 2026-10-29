from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm6 import mind_splash, silent_waves_passive

card = PokemonCardDef(
    guid="967d8b86-2295-5d56-9908-ff06c9b1e875",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name",
    display_name="Mesprit",
    searchable_by=["Mesprit", "Basic", "Mesprit"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=481,
    abilities=[
        Ability(
            title="Silent Waves",
            game_text="If you have Azelf in play, your opponent's Pok\u00e9mon in play have no Resistance.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=silent_waves_passive,
        ),
        Attack(
            title="Mind Splash",
            game_text="If Uxie is on your Bench, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=mind_splash,
        ),
    ],
)
