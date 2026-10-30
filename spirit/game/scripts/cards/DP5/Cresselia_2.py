"""STUB: effect not implemented — do not guess mechanics.
Cresselia (DP5 #2): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.dp import dp3_natu_96_future_sight


card = PokemonCardDef(
    guid="7054406c-c836-5b75-9154-fe6df258caf4",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cresselia.Name",
    display_name="Cresselia",
    searchable_by=["Cresselia", "Basic", "Cresselia"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="DP5",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=488,
    abilities=[
        Attack(
            title="Future Sight",
            game_text="Look at the top 5 cards of either player's deck and put them back on top of that player's deck in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=dp3_natu_96_future_sight(),
        ),
        Attack(
            title="Healing Light",
            game_text="Remove 1 damage counter from each of your Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            # STUB: attack effect not implemented
            effect=unimplemented,
        ),
    ],
)