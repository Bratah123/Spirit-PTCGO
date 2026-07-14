from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class OverheaterPassive(Passive):
    def blocks_burn_recovery(self, pokemon, carrier):
        return pokemon.owning_player_id != carrier.owning_player_id


card = PokemonCardDef(
    guid="f61cb59b-d8ab-5de7-924e-ea9da902a205",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1", "Centiskorch"],
    subtypes=["Stage 1"],
    collector_number=30,
    set_code="SWSH5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Ability(
            title="Overheater",
            game_text="Whenever your opponent flips a coin for their Burned Pokémon during Pokémon Checkup, it doesn't recover from that Special Condition even if the result is heads.",
            passive=OverheaterPassive(),
        ),
        Attack(
            title="Bursting Inferno",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=condition_attack(SpecialConditions.BURNED),
        ),
    ],
)
