from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack, recoil_attack

card = PokemonCardDef(
    guid="54717133-93ac-5126-b97d-98e5a2323066",
    key="SWSH9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AggronVMAX.Name",
    display_name="Aggron VMAX",
    searchable_by=["Aggron VMAX", "VMAX", "AggronVMAX"],
    subtypes=["VMAX"],
    collector_number=97,
    set_code="SWSH9",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.VMAX,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AggronV.Name",
    family_id=306,
    abilities=[
        Attack(
            title="Cracking Stomp",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=mill_attack(1),
        ),
        Attack(
            title="Max Take Down",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=270,
            effect=recoil_attack(30),
        ),
    ],
)