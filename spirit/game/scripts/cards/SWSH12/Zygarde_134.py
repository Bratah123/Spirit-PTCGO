from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import attach_from_discard
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.passives_common import is_in_active_spot

card = PokemonCardDef(
    guid="18232951-426c-5481-a3d1-9a4b9f349b5f",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=134,
    set_code="SWSH12",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=718,
    abilities=[
        Attack(
            title="Shout of Power",
            game_text="Attach a basic Energy card from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=attach_from_discard(
                predicate=is_basic_energy_card, count=1,
                target=lambda p: not is_in_active_spot(p),
                prompt="Choose a Benched Pokémon to attach the Energy to.",
            ),
        ),
        Attack(
            title="Speed Attack",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIGHTING: 1},
            damage=70,
        ),
    ],
)