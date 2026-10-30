from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import mill_scaled_damage
from spirit.game.card_effects.pokemon import is_energy_card
from spirit.game.card_effects.ecard import incinerate


def _is_fire_energy_card(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIRE.value in types


card = PokemonCardDef(
    guid="d20fe9cc-8874-55b9-9510-6a8c23366822",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkQuilava.Name",
    display_name="Dark Quilava",
    searchable_by=["Dark Quilava", "Stage 1", "DarkQuilava"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Incinerate",
            game_text="Show the top card of your opponent's deck to all players. If it's a Trainer card, discard it.",
            cost={PokemonTypes.FIRE: 1},
            effect=incinerate,
        ),
        Attack(
            title="Rushing Magma",
            game_text="Discard the top 5 cards of your deck. (If there are fewer than 5 cards in your deck, discard all of them.) This attack does 20 damage for each Fire Energy card you discarded in this way.",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            damage_operator="x",
            effect=mill_scaled_damage(5, 20, pred=_is_fire_energy_card),
        ),
    ],
)
