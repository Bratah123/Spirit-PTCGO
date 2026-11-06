from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import neutral_shield_passive


card = PokemonCardDef(
    guid="f8a6f5d9-a0b5-557f-905a-bdb66b6cf1ff",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Neutral Shield",
            game_text="Prevent all effects of attacks, including damage, done to Mew by Evolved Pok\u00e9mon. You can't use this power if Mew is Asleep, Confused, or Paralyzed.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=neutral_shield_passive,
        ),
        Attack(
            title="Psyshock",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
