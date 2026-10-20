"""STUB: effect not implemented — do not guess mechanics.
Ditto (Promo_XY #XY40): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="ad9d7205-fd76-5fda-80c2-6f9cddae0abe",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ditto.Name",
    display_name="Ditto",
    searchable_by=["Ditto", "Basic", "Ditto"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="Metamorphosis Gene",
            game_text="If this Pok\u00e9mon is your Active Pok\u00e9mon, it can use the attacks of your opponent's Active Pok\u00e9mon. (You still need the necessary Energy to use each attack.)",
            # STUB: ability effect not implemented
            effect=unimplemented,
        ),
        Attack(
            title="Stick On",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            # STUB: attack effect not implemented
            effect=attach_from_discard(predicate=is_basic_energy_card, count=1, target='self', prompt='Choose a basic Energy card to attach.'),
        ),
    ],
)