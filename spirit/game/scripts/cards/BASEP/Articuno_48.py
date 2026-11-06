from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import aurora_veil_passive


card = PokemonCardDef(
    guid="3d8209a6-2261-58a8-be36-31eb3208e093",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articuno.Name",
    display_name="Articuno",
    searchable_by=["Articuno", "Basic", "Articuno"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=144,
    abilities=[
        Ability(
            title="Aurora Veil",
            game_text="As long as Articuno is your Active Pok\u00e9mon, your Benched Pok\u00e9mon do not take damage from and are not affected by attacks. This power cannot be used if Articuno is affected by a Special Condition.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=aurora_veil_passive,
        ),
        Attack(
            title="Ice Beam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
