from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import flip_bonus, condition_attack


card = PokemonCardDef(
    guid="14aa6275-0327-5af2-a913-7033befcc228",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2", "Dustox"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Attack(
            title="Hazardous Scales",
            game_text="The Defending Pok\u00e9mon is now Asleep, Burned, and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=condition_attack(SpecialConditions.ASLEEP, SpecialConditions.BURNED, SpecialConditions.POISONED),
        ),
        Attack(
            title="Aerial Ace",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)