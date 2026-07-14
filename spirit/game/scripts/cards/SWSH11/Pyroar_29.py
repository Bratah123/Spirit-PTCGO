from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class ScorchingAuraPassive(Passive):
    def modify_burn_counters(self, counters, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 4
        return counters


card = PokemonCardDef(
    guid="5ab3f627-e8a9-53d1-bf94-d55f130bf78b",
    key="SWSH11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pyroar.Name",
    display_name="Pyroar",
    searchable_by=["Pyroar", "Stage 1", "Pyroar"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SWSH11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name",
    family_id=667,
    abilities=[
        Ability(
            title="Scorching Aura",
            game_text="During Pok\u00e9mon Checkup, put 4 damage counters on your opponent's Burned Pok\u00e9mon instead of 2.",
            passive=ScorchingAuraPassive(),
        ),
        Attack(
            title="Fire Fang",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
    ],
)