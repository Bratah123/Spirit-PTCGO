from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import energy_provides_type


def _metal_energy(card):
    return energy_provides_type(card, PokemonTypes.METAL.value)


card = PokemonCardDef(
    guid="05407f6e-226e-5b1a-9ec8-3fb9803a2e72",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=23,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Metal Load",
            game_text="Search your discard pile for a Metal Energy card and attach it to Metang.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=_metal_energy, count=1, target="self", minimum=0,
                prompt="Choose a Metal Energy card to attach."),
        ),
        Attack(
            title="Metal Claw",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
