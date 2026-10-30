"""STUB: effect not implemented — do not guess mechanics.
Dark Celebi (EX5 #4): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, unimplemented
from spirit.game.attributes import AbilityTypes, PokemonStage, PokemonTypes, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ex import dark_provide, poke_power_condition


card = PokemonCardDef(
    guid="e164b500-ca2b-5f4b-a412-09c64435b64f",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkCelebi.Name",
    display_name="Dark Celebi",
    searchable_by=["Dark Celebi", "Basic", "DarkCelebi"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="EX5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.GRASS, PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Dark Provide",
            game_text="Attach up to 1 Grass or Darkness Energy card from your hand to your Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_POWER,
            activation=Activations.ONCE_PER_TURN,
            condition=poke_power_condition(),
            effect=dark_provide(),
        ),
        Attack(
            title="Leaf Poison",
            game_text="The Defending Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.DARKNESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)