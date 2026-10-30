"""STUB: effect not implemented — do not guess mechanics.
Shining Jirachi (SL #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sl import stellar_reign

card = PokemonCardDef(
    guid="6e4c15e7-296e-5570-a9ae-2dde1126dc1f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningJirachi.Name",
    display_name="Shining Jirachi",
    searchable_by=["Shining Jirachi", "Basic", "ShiningJirachi"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="SL",
    rarity=Rarities.Shining,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=385,
    abilities=[
        Attack(
            title="Stellar Reign",
            game_text="If your opponent's Active Pok\u00e9mon is an evolved Pok\u00e9mon, devolve it by putting all of the Evolution cards on it into your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=stellar_reign,
        ),
    ],
)