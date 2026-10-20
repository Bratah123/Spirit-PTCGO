from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.support_common import switch_self_attack
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="5a04e26b-d2b3-5aac-b044-5e2d8efa1bfd",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name",
    display_name="Gliscor",
    searchable_by=["Gliscor", "Stage 1", "Gliscor"],
    subtypes=["Stage 1"],
    collector_number=81,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name",
    family_id=207,
    abilities=[
        Attack(
            title="Poison Ring",
            game_text="The Defending Pok\u00e9mon is now Poisoned. The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=condition_attack(SpecialConditions.POISONED, no_retreat=True),
        ),
        Attack(
            title="Night Slash",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(),
        ),
    ],
)