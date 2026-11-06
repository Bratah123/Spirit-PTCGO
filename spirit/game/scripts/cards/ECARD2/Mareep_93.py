from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="1df13bfb-b45f-59b5-a381-777658fa6bc2",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name",
    display_name="Mareep",
    searchable_by=["Mareep", "Basic", "Mareep"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=179,
    abilities=[
        Attack(
            title="Charge",
            game_text="Attach 1 Lightning Energy card from your discard pile to Mareep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=lambda c: is_basic_energy_card(c)
                and energy_provides_type(c, PokemonTypes.LIGHTNING.value),
                count=1, target="self",
                prompt="Choose a Lightning Energy card to attach to Mareep",
            ),
        ),
        Attack(
            title="Tail Slap",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
