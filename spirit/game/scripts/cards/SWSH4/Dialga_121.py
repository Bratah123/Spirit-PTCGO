from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_metal_energy_card
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="da2623da-5a2d-59bd-a04a-0350509f6da7",
    key="SWSH4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name",
    display_name="Dialga",
    searchable_by=["Dialga", "Basic", "Dialga"],
    subtypes=["Basic"],
    collector_number=121,
    set_code="SWSH4",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=483,
    abilities=[
        Attack(
            title="Rewind Time",
            game_text="Attach up to 2 Metal Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(
                predicate=is_metal_energy_card, count=2, minimum=0, target="choice",
                prompt="Choose up to 2 Metal Energy cards to attach",
            ),
        ),
        Attack(
            title="Flash of Destruction",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
