from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.pokemon import rock_crush
from spirit.game.card_effects.sm6 import tyrannical_heart_passive

card = PokemonCardDef(
    guid="b231c794-64fc-50fc-bab7-7d5da60f6b04",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 2", "Tyrantrum"],
    subtypes=["Stage 2"],
    collector_number=69,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    family_id=696,
    abilities=[
        Ability(
            title="Tyrannical Heart",
            game_text="As long as you don't have more Pok\u00e9mon in play than your opponent, this Pok\u00e9mon's attacks do 60 more damage (before applying Weakness and Resistance), and it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=tyrannical_heart_passive,
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=rock_crush,
        ),
    ],
)
