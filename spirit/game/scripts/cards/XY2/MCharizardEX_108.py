from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack


card = PokemonCardDef(
    guid="457015af-1b74-5f4d-912e-f9542ecbe70d",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MCharizardEX.Name",
    display_name="M Charizard-EX",
    searchable_by=["M Charizard-EX", "MEGA", "EX", "MCharizardEX"],
    subtypes=["MEGA", "EX"],
    collector_number=108,
    set_code="XY2",
    rarity=Rarities.RareSecret,
    hp=230,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name",
    family_id=6,
    abilities=[
        Attack(
            title="Wild Blaze",
            game_text="Discard the top 5 cards of your deck.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=mill_attack(5, opponent=False),
        ),
    ],
)