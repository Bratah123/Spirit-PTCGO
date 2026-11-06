from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import attach_hand_energy, energy_splash
from spirit.game.card_effects.trainers import is_basic_energy_card


card = PokemonCardDef(
    guid="32a9477c-d2f3-5e02-8b81-6fd57cce172a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Politoed.Name",
    display_name="Politoed",
    searchable_by=["Politoed", "Stage 2", "Politoed"],
    subtypes=["Stage 2"],
    collector_number=173,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Sudden Growth",
            game_text="Attach any number of basic Energy cards from your hand to Politoed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_hand_energy(count=99, predicate=is_basic_energy_card),
        ),
        Attack(
            title="Frog Hop",
            game_text="Flip a coin. If heads, this attack does 30 damage plus 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Energy Splash",
            game_text="Move 2 Water Energy cards attached to Politoed to 1 or 2 of your Benched Pok\u00e9mon. (You may put both on the same Pok\u00e9mon or 1 each on 2 different Pok\u00e9mon.) If you have no Benched Pok\u00e9mon, ignore this effect.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=energy_splash,
        ),
    ],
)
