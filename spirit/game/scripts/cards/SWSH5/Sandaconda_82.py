from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_scaled_damage
from spirit.game.card_effects.pokemon import is_energy_card


def _is_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_energy_card(card) and PokemonTypes.FIGHTING.value in types


card = PokemonCardDef(
    guid="298d1d7f-9206-5fd0-a53d-d09c1173194a",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1", "Sandaconda"],
    subtypes=["Stage 1"],
    collector_number=82,
    set_code="SWSH5",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Big Sand Cannon",
            game_text="Discard the top 6 cards of your deck. This attack does 60 damage for each Fighting Energy card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=60,
            damage_operator="x",
            effect=mill_scaled_damage(6, 60, pred=_is_fighting_energy),
        ),
        Attack(
            title="Skull Bash",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)