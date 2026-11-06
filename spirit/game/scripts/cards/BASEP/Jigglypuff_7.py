from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.support_common import heal_attack


card = PokemonCardDef(
    guid="96f5f79c-cd2c-5da3-951e-096602a6a9b3",
    key="BASEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="BASEP",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=39,
    abilities=[
        Attack(
            title="First Aid",
            game_text="Remove 1 damage counter from Jigglypuff.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(10),
        ),
        Attack(
            title="Double-edge",
            game_text="Jigglypuff does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=recoil_attack(20),
        ),
    ],
)
