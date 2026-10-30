from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import psychic_damage, time_travel_passive


card = PokemonCardDef(
    guid="6b295de6-1d13-5c80-8bf5-c51d231e64f9",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name",
    display_name="Celebi",
    searchable_by=["Celebi", "Basic", "Celebi"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=251,
    abilities=[
        Ability(
            title="Time Travel",
            game_text="If an opponent's attack would Knock Out Celebi, flip a coin. If heads, Celebi isn't Knocked Out and you shuffle it and all cards attached to it into your deck. This power doesn't work if Celebi is already Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=time_travel_passive,
        ),
        Attack(
            title="Psychic Damage",
            game_text="Flip 3 coins. For each heads, put 1 damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=psychic_damage,
        ),
    ],
)
