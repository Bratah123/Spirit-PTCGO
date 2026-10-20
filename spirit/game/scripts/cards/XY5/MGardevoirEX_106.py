from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per, count_energy




card = PokemonCardDef(
    guid="13583a61-52d9-51c7-8363-ba2ccb331884",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name",
    display_name="M Gardevoir-EX",
    searchable_by=["M Gardevoir-EX", "MEGA", "EX", "MGardevoirEX"],
    subtypes=["MEGA", "EX"],
    collector_number=106,
    set_code="XY5",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name",
    family_id=282,
    abilities=[
        Attack(
            title="Brilliant Arrow",
            game_text="This attack does 30 damage times the amount of Fairy Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_energy('mine', energy_type=PokemonTypes.FAIRY), 30),
        ),
    ],
)