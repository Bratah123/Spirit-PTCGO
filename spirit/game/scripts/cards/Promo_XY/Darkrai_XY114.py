from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


card = PokemonCardDef(
    guid="ab725d63-7db3-523c-adeb-c7f83f0fd528",
    key="Promo_XY",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darkrai.Name",
    display_name="Darkrai",
    searchable_by=["Darkrai", "Basic", "Darkrai"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="Promo_XY",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=491,
    abilities=[
        Attack(
            title="Dark Cutter",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Abyssal Sleep",
            game_text="Your opponent's Active Pok\u00e9mon is now Asleep. Your opponent flips 2 coins instead of 1 between turns. If either of them is tails, that Pok\u00e9mon is still Asleep.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=condition_attack(SpecialConditions.ASLEEP, checkup_coins=2),
        ),
    ],
)