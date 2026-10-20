from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ancient_traits import ancient_trait
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.card_effects.passives_common import takes_less_passive


card = PokemonCardDef(
    guid="629ec02d-5c47-53e3-88ed-b916d41fc688",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyperior.Name",
    display_name="Rhyperior",
    searchable_by=["Rhyperior", "Stage 2", "Rhyperior"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="XY5",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    family_id=111,
    abilities=[
        ancient_trait('Ω Barrier'),
        Ability(
            title="Rock Wall",
            game_text="Any damage done to your Pok\u00e9mon by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            passive=takes_less_passive(10, protects='team'),
        ),
        Attack(
            title="Hammer Arm",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=mill_attack(1),
        ),
    ],
)