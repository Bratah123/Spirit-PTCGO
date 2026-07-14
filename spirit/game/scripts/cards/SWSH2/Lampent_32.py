from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from spirit.game.card_effects.pokemon import top_entry
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import attach_from_discard


def _is_fire_energy(card):
    # "a Fire Energy card" = a BASIC Fire Energy (Welder precedent) -- Heat
    # Fire Energy carries POKEMON_TYPES=[Fire] but is Special.
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.FIRE.value in types


reignite = attach_from_discard(predicate=_is_fire_energy, count=1, target="choice")

card = PokemonCardDef(
    guid="129364d2-7c0c-53a9-b32c-56a94164de81",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1", "Lampent"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SWSH2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Top Entry",
            trigger=Triggers.ON_TURN_DRAWN,
            game_text="Once during your turn, if you drew this Pok\u00e9mon from your deck at the beginning of your turn and your Bench isn't full, before you put it into your hand, you may put it onto your Bench.",
            effect=top_entry(),
        ),
        Attack(
            title="Reignite",
            game_text="Attach a Fire Energy card from your discard pile to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=reignite,
        ),
    ],
)