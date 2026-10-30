from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.pokemon import energy_provides_type


def _metal_energy(card):
    return energy_provides_type(card, PokemonTypes.METAL.value)


card = PokemonCardDef(
    guid="2729f87f-2ac4-51d5-b7cf-345d2c75a808",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="EX5",
    rarity=Rarities.Rare,
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
