from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="84313284-563f-5100-8a4a-6c5a20b54281",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    display_name="Flaaffy",
    searchable_by=["Flaaffy", "Stage 1", "Flaaffy"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Energy Recall",
            game_text="Attach up to 2 basic Energy cards from your discard pile to Flaaffy.",
            cost={PokemonTypes.LIGHTNING: 1},
            # STUB: attack effect not implemented
            effect=attach_from_discard(predicate=is_basic_energy_card, count=2, target="self", minimum=0),
        ),
        Attack(
            title="Lightning Ball",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)