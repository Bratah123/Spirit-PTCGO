from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="3d9e30f1-37e0-5c8f-9940-d44b4ee34b10",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    display_name="Kadabra",
    searchable_by=["Kadabra", "Stage 1", "Kadabra"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Energy Recall",
            game_text="Attach 2 basic Energy cards from your discard pile to Kadabra (1 if you have only 1).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=2, target="self",
                minimum=None,
            ),
        ),
        Attack(
            title="Confuse Ray",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)
