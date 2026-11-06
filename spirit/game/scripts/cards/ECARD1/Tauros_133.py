from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, recoil_attack


card = PokemonCardDef(
    guid="1f7b5a5e-289b-5ad7-99f1-1bb1f3db15c0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Horn Hazard",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Take Down",
            game_text="Tauros does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=recoil_attack(20),
        ),
    ],
)
