from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class _CalmingAroma(Passive):
    """Each of your Pokemon's attacks costs Fairy less."""
    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != carrier.owning_player_id or cost.get("Fairy", 0) <= 0:
            return cost
        cost["Fairy"] -= 1
        if cost["Fairy"] <= 0:
            del cost["Fairy"]
        return cost


card = PokemonCardDef(
    guid="287a701b-8d36-53bf-a705-b7f8f060a745",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Florges.Name",
    display_name="Florges",
    searchable_by=["Florges", "Stage 2", "Florges"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="XY8",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Floette.Name",
    family_id=669,
    abilities=[
        Ability(
            title="Calming Aroma",
            game_text="Each of your Pok\u00e9mon's attacks costs Fairy less.",
            passive=_CalmingAroma(),
        ),
        Attack(
            title="Wonder Shine",
            game_text="Your opponent's Active Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.FAIRY: 3},
            damage=70,
            effect=condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)