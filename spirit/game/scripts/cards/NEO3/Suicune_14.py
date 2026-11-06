from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import aurora_wave, crystal_body_passive


card = PokemonCardDef(
    guid="19403144-d856-5231-8f84-5105ce2c6b7b",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=245,
    abilities=[
        Ability(
            title="Crystal Body",
            game_text="Prevent all effects of your opponent's attacks, other than damage, done to Suicune. This power stops working while Suicune is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=crystal_body_passive,
        ),
        Attack(
            title="Aurora Wave",
            game_text="Flip 2 coins. If both are heads, the Defending Pok\u00e9mon is now Paralyzed. If only 1 is heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 3},
            damage=30,
            effect=aurora_wave,
        ),
    ],
)
