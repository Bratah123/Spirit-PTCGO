from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.ex import rage_damage


card = PokemonCardDef(
    guid="125c21de-ad18-567c-b01c-16f859393ac2",
    key="POP2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="POP2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Rage",
            game_text="Does 10 damage plus 10 more damage for each damage counter on Tauros.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=rage_damage(10, 10),
        ),
        Attack(
            title="Take Down",
            game_text="Tauros does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)
