from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import spread_damage
from spirit.game.session.passives import Passive


class SubmergePassive(Passive):
    def prevents_damage(self, calc, carrier):
        return calc.is_attack and calc.target is carrier and not calc.to_active


card = PokemonCardDef(
    guid="3952862f-a9b0-5bfc-bb13-a23b124a8273",
    key="SWSH2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1", "Whiscash"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SWSH2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Ability(
            title="Submerge",
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=SubmergePassive(),
        ),
        Attack(
            title="Earthquake",
            game_text="This attack also does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=140,
            effect=spread_damage(20, side="mine", also_base=True),
        ),
    ],
)
