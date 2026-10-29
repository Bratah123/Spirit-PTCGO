from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm5 import weather_guard_passive

card = PokemonCardDef(
    guid="afd2fde3-1be2-5b36-bb61-595e7a85f6a7",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Weather Guard",
            game_text="Your Grass Pok\u00e9mon have no Weakness.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=weather_guard_passive,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)