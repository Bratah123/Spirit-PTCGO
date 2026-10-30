"""STUB: effect not implemented — do not guess mechanics.
Carvanha (EX16 #47): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.data_utils import Triggers
from spirit.game.card_effects.ex import rough_skin


card = PokemonCardDef(
    guid="5bacd979-df1c-5f31-bad6-3b39d1af1fea",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic", "Carvanha"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="EX16",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=318,
    abilities=[
        Ability(
            title="Rough Skin",
            game_text="If Carvanha is your Active Pok\u00e9mon and is damaged by an opponent's attack (even if Carvanha is Knocked Out), put 1 damage counter on the Attacking Pok\u00e9mon.",
            ability_type=AbilityTypes.POKE_BODY,
            # STUB: ability effect not implemented
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=rough_skin(1),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)