from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.session.passives import Passive


class BodyguardPassive(Passive):
    """Prevent all effects of attacks done to you or your hand by your
    opponent's Pokemon (the engine's player/hand shield; attack-made play
    locks already on you switch off)."""

    def blocks_player_attack_effects(self, affected_player_id, carrier):
        return affected_player_id == carrier.owning_player_id


card = PokemonCardDef(
    guid="b49d7f42-e18a-5092-b10c-4ad8a5fcd66b",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1", "Marowak"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=105,
    abilities=[
        Ability(
            title="Bodyguard",
            game_text="Prevent all effects of attacks done to you or your hand by your opponent's Pok\u00e9mon. Remove any existing effects.",
            passive=BodyguardPassive(),
        ),
        Attack(
            title="Bonemerang",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=60),
        ),
    ],
)