from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack, recoil_attack


card = PokemonCardDef(
    guid="22f0b2c2-bd7c-562b-a83f-141bdca106e6",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name",
    display_name="Poliwrath",
    searchable_by=["Poliwrath", "Stage 2", "Poliwrath"],
    subtypes=["Stage 2"],
    collector_number=17,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name",
    family_id=60,
    abilities=[
        Attack(
            title="Steamroll",
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Submission",
            game_text="This Pok\u00e9mon does 30 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=recoil_attack(30),
        ),
    ],
)